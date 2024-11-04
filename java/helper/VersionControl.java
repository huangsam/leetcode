package helper;

import java.util.Random;

public abstract class VersionControl {
    private final int culpritVersion;
    public VersionControl() {
        culpritVersion = new Random().nextInt(100);
    }
    public boolean isBadVersion(int version) {
        return version >= culpritVersion;
    }
}
